# Safe Net Universal version 

Utilizes Man-In-The-Middle to intercept and modify requests on the fly.

# Working

1. User installs CA certificate of our mitmproxy and modifies his primary DNS server to that of our own DNS spoofer.
2. DNS proxy responds with the proxy's IP address for all A queries.
3. The mitmproxy acts as a reverse proxy and opens upstream connections to actual servers and relaays their responses to clients.
4. When the response contains images, the images are put thruough a computer vision model to classify them and are modified on the fly.
