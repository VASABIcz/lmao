import fbchat
import asyncio
import datetime
from cfg import *

times = (
    ((8, 25), (9, 15), (10, 5), (11, 10), (12, 5), (13, 0)),
    ((8, 25), (9, 15), (10, 5), (11, 10), (12, 5), (13, 55), (14, 50), (15, 40)),
    ((8, 25), (9, 15), (10, 5), (11, 10), (12, 5), (13, 0)),
    ((8, 25), (9, 15), (10, 5), (11, 10), (12, 5), (13, 0)),
    ((8, 25), (9, 15), (10, 5), (11, 10), (12, 5), (13, 0)),
)

async def main():
    session = await fbchat.Session.login(EMAIL, PASSWORD)
    print("Own id: {}".format(session.user.id))
    user = fbchat.User(session=session, id=WHO)

    await user.send_text("VASABI bot on duty")


    while True:
        day = datetime.datetime.today()
        if day.weekday() == 5 or day.weekday() == 6:
            print(f"its {day.weekday()+1} weakday waiting for next day")
            await asyncio.sleep((datetime.datetime(day.year, day.month, day.day+1, 1) - day).total_seconds())
            continue


        idk = times[day.weekday()]
        for lesson in idk:
            future = datetime.datetime(day.year, day.month, day.day, lesson[0], lesson[1])
            sex = (future - day).total_seconds()
            if sex <= 0:
                print(f"lesson already happened skipping: {lesson}")
                continue

            print(f"waiting for next lesson {lesson}")
            await asyncio.sleep(sex)
            await user.send_text("za 5 min konci hodina :D")
            await asyncio.sleep(2)
            await user.send_text("za 5 min konci hodina :D")
            await asyncio.sleep(2)
            await user.send_text("za 5 min konci hodina :D")

        else:
            print(f"lessons for this day done waiting for next day")
            await asyncio.sleep((datetime.datetime(day.year, day.month, day.day+1, 1) - day).total_seconds())



if __name__ == '__main__':
    asyncio.run(main())