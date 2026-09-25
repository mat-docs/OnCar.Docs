# Configuration API

System Monitor includes a Configuration API: a network API, based on a [gRPC](https://grpc.io/) interface defined with protobuf files, for ECU programming and monitoring through System Monitor. Clients can be written in any language with gRPC support, such as C#, C++, Python, Java or Go, and can run on the same PC as System Monitor or elsewhere on the network.

The API is provided by the Configuration Service (`SysMonConfigurationService.exe`), which is installed with System Monitor in its `Configuration Service` folder. The service runs alongside System Monitor and passes requests to it through the System Monitor COM (ActiveX) API.

- Calls to the API are handled one at a time; a call waits until earlier requests have completed.
- Measurement parameter values can be cached in the service to give the fastest possible response to requests for many values. Cached requests are not blocked by other actions. The cache update rate is configurable.
- Connections use HTTPS. Clients can optionally be required to authenticate with a token from an OAuth provider.

## Starting and stopping the API

The API is turned off by default. It is enabled and configured in the [Configuration API Setup](configuration-api-setup.md) dialog box (**Tools** > **Configuration API Setup** > **Configuration API Setup**).

When enabled, the API starts automatically when System Monitor starts, and stops when System Monitor closes. It can also be controlled while System Monitor is running, from **Tools** > **Configuration API Setup** or by right-clicking the API panel of the status bar:

- **Configuration API Start** - Start the API. Available when the API is enabled and not running.
- **Configuration API Stop** - Stop the API. Available when the API is running.
- **Configuration API Reset** - Stop the API if it is running, and start it again. Available when the API is enabled.

## API status

When the API is enabled, its address, port and status are shown in the status bar, for example **API: https://127.0.0.1:7000 ON**. The panel colour shows the status:

| Status | Colour | Meaning |
|---|---|---|
| **ON** | Green | The API is running with the configured SSL certificate. |
| **NO CERT** | Yellow | The API is running, but no SSL certificate is configured, so a default development certificate is used. |
| **OFF** | Red | The API failed to start or has stopped. |
| **NOT FOUND** | Red | The Configuration Service was not found in the System Monitor installation. |

The service writes its own log file (named `API_...`) in the System Monitor log folder (**Help** > **View Log Folder**).

## Developing a client

A client can be developed using either the API DLL or the protobuf files available in the Configuration API NuGet package. The messages and services are described in [Protocol Documentation](protocol-documentation.md). **Help** > **Configuration API Documentation** opens the online Configuration API documentation.

An example gRPC client written in C#, with sample code for every method exposed by the API, is available on GitHub: [System.Monitor.Configuration.API.Client.Sample](https://github.com/mat-docs/System.Monitor.Configuration.API.Client.Sample).

**See also:** [Configuration API Setup](configuration-api-setup.md); [Protocol Documentation](protocol-documentation.md); [ActiveX Automation](../activex-automation/index.md)
