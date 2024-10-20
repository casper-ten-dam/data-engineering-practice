import psycopg2
import pathlib


def main():
    host = "postgres"
    database = "postgres"
    user = "postgres"
    pas = "postgres"
    conn = psycopg2.connect(host=host, database=database, user=user, password=pas)
    # your code here
    with conn.cursor() as cur:
        # create the table
        # TODO: consider varchar lengths, zip code to INT?, map date to date?
        cur.execute(
            "CREATE TABLE accounts (customer_id serial PRIMARY KEY, first_name VARCHAR, last_name VARCHAR, address_1 VARCHAR, address_2 VARCHAR, city VARCHAR, state VARCHAR, zip_code VARCHAR, join_date VARCHAR)"
        )
        cur.commit()
        # insert the data from the csv file
        # TODO: fix, doesnt work as data is not in docker build
        cur.execute(
            """
COPY accounts(customer_id, first_name, last_name, address_1, address_2, city, state, zip_code, join_date)
FROM %(accounts_csv_path)s
DELIMITER ','
CSV HEADER;
""",
            {"accounts_csv_path": str(pathlib.Path.cwd() / "data" / "accounts.csv")},
        )


if __name__ == "__main__":
    main()
