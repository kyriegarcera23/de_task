from main import Main
import schedule
import time

if __name__ == "__main__":
    main_instance  = Main()
    schedule.every().day.at("07:00").do(main_instance.process)
    while True:
        schedule.run_pending()
        time.sleep(1)