var builder = WebApplication.CreateBuilder(args);

var app = builder.Build();

app.UseHttpsRedirection();

var count = 123456789;

app.MapGet("/booking_reference", () =>
{
    count++;
    return count.ToString("x");
});

app.Run();
