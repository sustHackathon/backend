import time
import psycopg2
import config
import utils
import sched

import schemas

import datetime


# Database connection parameters
db_params = {
    'dbname': "sustHackathon",
    'user': config.Settings.database_username,
    'password': config.Settings.database_password,
    'host': config.Settings.database_hostname,
    'port': config.Settings.database_port,
}


def job(sc):
    try:
        # Connect to the database
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        if conn is None:
            print("Error in connecting to the database")
            return

        # Get current date and time
        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute

        # Fetch scheduled emails from the database
        query = f"SELECT * FROM schedulemails"
        cursor.execute(query)
        scheduled_mails = cursor.fetchall()

        for mail in scheduled_mails:

            # Assuming the columns order: id, subject, body, date, time, email
            mail_id, place, date, mail_time, email = mail
            scheduled_mail = schemas.ScheduleMail(
                place=place, date=date, time=mail_time)
            # Now you can use scheduled_mail attributes to send the email

            if date == datetime.datetime.now().date() and mail_time == f"{hour}:{minute}":

                utils.sendEmail(
                    "Scheduled Email",
                    f"Hello, This is a scheduled email from TripMate. You are scheduled to visit {place} today at {mail_time}.",
                    email
                )
                query = f"DELETE FROM schedulemails WHERE id = {mail_id}"
                cursor.execute(query)
                print(f"Email sent to {email} at {mail_time} on {date}")

        # Commit changes and close the database connection
        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error in job: {e}")

    # Reschedule the job every minute
    sc.enter(60, 1, job, (sc,))


def main():
    s = sched.scheduler(time.time, time.sleep)
    # Schedule the job to start immediately
    s.enter(0, 1, job, (s,))

    # Run the scheduler
    s.run()


if __name__ == "__main__":
    main()
