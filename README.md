# Minecraft Server

This application is used to demonstrate Stackato's Harbor and FileSystem services.

When this application starts running, the latest vanilla Minecraft server from http://minecraft.net is retrieved and starts running. A WSGI web application reads the environment variables from the session, and displays the connection string for the Minecraft client in the webapp.

Minecraft's world data is persistent, held by FileSystem's services. It will be reloaded if the app is stopped or restarted. Harbor is used to provision a TCP port (4100 by default) to Minecraft.

## Deploying to Stackato

    stackato push -n

## Find the URL

 * open up the web application
 * take note of the credentials show on the page
 * run 'stackato run "tail server.log --follow"' to check if the minecraft server is up
 * connect using your minecraft client
 * craft away!
