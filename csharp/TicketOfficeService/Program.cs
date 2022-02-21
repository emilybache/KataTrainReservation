using TicketOfficeService;

var builder = WebApplication.CreateBuilder(args);

var app = builder.Build();

app.UseHttpsRedirection();

app.MapPost("/reserve", (ReserveRequest request) =>
{
    var ticketOffice = new TicketOffice();
    var reservationRequest = new ReservationRequest(request.train_id, request.seat_count);
    var reservation = ticketOffice.MakeReservation(reservationRequest);
    
    return Results.Ok(reservation);
});

app.Run();

record ReserveRequest(string train_id, int seat_count);