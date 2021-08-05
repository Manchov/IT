#See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging .

FROM mcr.microsoft.com/dotnet/aspnet:5.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
WORKDIR /src
COPY ["ServiceNet.csproj", "."]
RUN dotnet restore "./ServiceNet.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "ServiceNet.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "ServiceNet.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "ServiceNet.dll"]