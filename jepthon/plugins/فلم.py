#Jepthon ©
#By Reda 
from imdb import Cinemagoer
import requests
from html_telegraph_poster.upload_images import upload_image
from random import randint
from jepthon import jepiq
import asyncio
from ..core.managers import edit_delete, edit_or_reply
ia = Cinemagoer()

@jepiq.ar_cmd(pattern="فلم")
async def rfilm(event):
    await event.edit("يرجى الانتضار جاري البحث على فلم...")
    for _ in range(100):
        movieID = randint(1,250)
        movieT = ia.get_top250_movies()

        movie = movieT[movieID]
        year = movie.get('year')
        rating = movie.get('rating', "لا يوجد")
        movien = movie.get('title')
        movies = ia.search_movie(str(movien))
        if len(movies) < 3:
            return await edit_delete(event, "**حدث خطأ حاول مجدداً **")
        movief = movies[0] 
        moviep = movief.get('full-size cover url')
        movied = movief.get('plot')
        if movied is None:
            movied = "-"
        if moviep is not None:
            moviep = upload_image(str(moviep)) 
        if moviep is None:
            moviep = f"https://telegra.ph/file/15480332b663adae49205.jpg"
        moviet = f"الاسم: {movien}\nالسنة: {year}\nالتقييم: {rating}\nالقصة: {movied}"
        await event.delete()
        await jepiq.send_file(
                event.chat_id,
                moviep,
                caption=moviet,
                )
        break
