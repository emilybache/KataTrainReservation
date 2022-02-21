using System.Text.Json;
using static Microsoft.AspNetCore.Http.Results;
using File = System.IO.File;

var builder = WebApplication.CreateBuilder(args);

var app = builder.Build();

app.UseHttpsRedirection();

var trains = GetTrains();

app.MapGet("/data_for_train/{trainId}", (string trainId) => trains[trainId]);

app.MapPost("/reserve", (ReserveRequest request) =>
{
    var train = trains[request.train_id];
    // Validate request
    foreach (var seat in request.seats)
    {
        if (!train.seats.ContainsKey(seat))
            return BadRequest($"seat not found {seat}");

        var existingReservation = train.seats[seat].booking_reference;
        
        if (!string.IsNullOrEmpty(existingReservation) && existingReservation != request.booking_reference)
            return BadRequest($"already booked with reference: {existingReservation}");
    }

    train.MakeReservation(request.seats, request.booking_reference);
    
    return Ok(train);
});

app.MapPost("/reset/{trainId}", (string trainId) =>
{
    var train = trains[trainId];
    train.Reset();
    
    return Ok(train);
});

app.Run();


Trains GetTrains()
{
    var allText = File.ReadAllText(@"trains.json");

    return JsonSerializer.Deserialize<Trains>(allText)!;
}
