using System.Text.Json;

var builder = WebApplication.CreateBuilder(args);

var app = builder.Build();

app.UseHttpsRedirection();

app.MapGet("/data_for_train/{train}", (string train) =>
{
    var trains = GetTrains();
    return train switch
    {
        "local_1000" => trains.local_1000,
        "express_2000" => trains.express_2000,
        _ => null
    };
});

app.Run();



Trains GetTrains()
{
    var allText = File.ReadAllText(@"trains.json");
    var trains = JsonSerializer.Deserialize<Trains>(allText)!;

    return trains;
}

public record Trains
{
    public object local_1000 { get; set; } = null!;
    public object express_2000 { get; set; } = null!;
}
