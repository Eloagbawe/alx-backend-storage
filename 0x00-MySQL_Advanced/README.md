solutions to mysql advanced exercises

0. Write a SQL script that creates a table users following these requirements:

    With these attributes:

        id, integer, never null, auto increment and primary key
        email, string (255 characters), never null and unique
        name, string (255 characters)

    If the table already exists, your script should not fail
    Your script can be executed on any database

    Context: Make an attribute unique directly in the table schema will enforce your business rules and avoid bugs in your application

1. Write a SQL script that creates a table users following these requirements:

    With these attributes:

        id, integer, never null, auto increment and primary key
        email, string (255 characters), never null and unique
        name, string (255 characters)
        country, enumeration of countries: US, CO and TN, never null (= default will be the first element of the enumeration, here US)

    If the table already exists, your script should not fail

    Your script can be executed on any database

2. Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans

    Requirements:

        Import this table dump: metal_bands.sql
        Column names must be: origin and nb_fans
        Your script can be executed on any database

    Context: Calculate/compute something is always power intensive… better to distribute the load!

3. Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

    Requirements:

        Import this table dump: metal_bands.sql.zip
        Column names must be: band_name and lifespan (in years)
        You should use attributes formed and split for computing the lifespan
        Your script can be executed on any database

4. Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

        Quantity in the table items can be negative.

        Context: Updating multiple tables for one action from your application can generate issue: network disconnection, crash, etc… to keep your data in a good shape, let MySQL do it for you!
