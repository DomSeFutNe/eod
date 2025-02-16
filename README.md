# README

## Initial project

- Backend
  - Create a virtual environment with python
  - Add a .env file to the backend (`backend/.env`) folder with content:
  ```dotenv
    // Django
    DJANGO_SECRET_KEY="" // Your django secret key
    DJANGO_DEBUG="True" // This environment variable should not be present in production or set to "False"
    DJANGO_ALLOWED_HOSTS="localhost,127.0.0.1"
    DJANGO_DB_NAME="" // Your database name
    DJANGO_DB_USER="" // Your database user
    DJANGO_DB_PASSWORD="" // Your database password
    DJANGO_DB_HOST="localhost"
    DJANGO_DB_PORT="5432"

    // Blizzard API
    BLIZZARD_CLIENT_ID="" // Your blizzard client id
    BLIZZARD_CLIENT_SECRET="" // Your blizzard client secret

    // Raid Helper API
    DISCORD_SERVER_ID="" // Your discord server id
    RAID_HELPER_API_KEY="" // Your raid helper api key
  ```
    - To get the blizzard client information, you have to login into [Blizzard Development Documentation](https://develop.battle.net/) and create a new API access.
    - To get the discord server id, go to your discord server which is connected with you raid-helper bot.  
    Inside the server settings got to `Widget`.  
    There you can copy your `SERVER-ID`.
    - To get the raid helper api key, go to your discord server which is connected to your raid-helper bot.  
    Go to the channel where the raid-helper bot have access.  
    Type into the chat `/apikey show` (If you never created an API key, you can create one with `/apikey refresh`).  
    To get the API key you need the administration permission on the discord server.