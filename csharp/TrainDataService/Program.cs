using System.Text.Json;

var builder = WebApplication.CreateBuilder(args);

var app = builder.Build();

app.UseHttpsRedirection();

var trains = GetTrains();

app.MapGet("/data_for_train/{train}", (string train) => trains[train]);

app.Run();



Trains GetTrains()
{
    var allText = File.ReadAllText(@"trains.json");
    var trains = JsonSerializer.Deserialize<Trains>(allText)!;

    return trains;
}
