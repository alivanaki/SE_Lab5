# SE_Lab5
# گزارش
برای انجام این آزمایش از فریم ورک جنگو برای پیاده‌سازی دو سرویس موردنظر استفاده کردیم. در این آزمایش سامانه موردنظر دارای دو سرویس به نام‌های data و user می‌باشد. هدف کلی از این دو سرویس نیز آن است که با استفاده از سرویس user اطلاعات مربوط به کاربر مانند آدرس ایمیل و نام کاربری آن را دریافت کنیم و با استفاده از سرویس data اطلاعات مربوطه و داده‌هایی را در سامانه ذخیره کند. در این آزمایش قصد داریم که این دو سرویس را بر روی docker بالا آورده و عملکرد آن‌ها را نشان دهیم. شایان ذکر است که این دو سرویس در قالب دو API پیاده‌سازی شده‌اند که برای پیاده‌سازی آن‌ها از ModelViewset استفاده شده است. با این کار هر یک از عملیات CRUD را می‌توانیم بر روی این دو سرویس انجام دهیم. بنابراین در کل دو سرویس user و data خواهیم داشت که این دو سرویس در قالب دو ModelViewset پیاده‌سازی شده‌اند و به همین دلیل تمام عملیات CRUD بر روی آن‌ها امکان‌پذیر می‌باشد.

 در تصاویر زیر می‌توانید مدل، سریالایزر و ویوی مربوط به سرویس user را مشاهده کنید.
 
![image](https://github.com/alivanaki/SE_Lab5/assets/58647313/e94aab27-bf9b-424c-90cb-a1620904e655)
![image](https://github.com/alivanaki/SE_Lab5/assets/58647313/3049858f-c7a9-48b6-87c5-e47ee543302b)

 در تصاویر زیر می‌توانید مدل، سریالایزر و ویوی مربوط به سرویس data را مشاهده کنید.

 ![image](https://github.com/alivanaki/SE_Lab5/assets/58647313/e3647167-5cd1-4403-9dfd-1f74b0b5367d)
![image](https://github.com/alivanaki/SE_Lab5/assets/58647313/fe5709f4-d042-41ca-a872-a12b508ec520)

توجه داشته باشید که برای این بخش از آزمایش دو مدل ساده و دو سرویس ساده را در نظر گرفتیم.

در ادامه برای هر یک از سرویس‌ها موردنظر DockerFile مربوطه را تعریف می‌کنیم. در تصویر زیر می‌توانید محتویات DockerFileهای مربوطه را مشاهده کنید.

![image](https://github.com/alivanaki/SE_Lab5/assets/58647313/12155cc4-b0a9-42a6-aeaa-88731791e853)
![image](https://github.com/alivanaki/SE_Lab5/assets/58647313/ab3e3111-0b73-421a-9fb3-a3077c7e08d1)

هم‌چنین در ادامه فایل docker-compose.yml را به شکل زیر تعریف می‌کنیم.

![image](https://github.com/alivanaki/SE_Lab5/assets/58647313/3d1051ce-8755-40e2-80de-3708a8a08bd5)

در نهایت با استفاده از دستور `docker-compose up` سرویس‌های موردنظر را بر روی داکر بالا می‌آوریم.

![Docker_compose2](https://github.com/alivanaki/SE_Lab5/assets/58647313/73a3090b-4891-46e7-822f-b7967b81e865)

هم‌چنین با استفاده از دستورهای `docker ps` و `docker image ls` وجود imageها و containerها مربوط به سرویس‌های خود را بررسی می‌کنیم.

![Docker_compose3](https://github.com/alivanaki/SE_Lab5/assets/58647313/ad8a992e-8022-4dfa-9961-19480807f62a)

در پایان نیز درستی عملکرد APIهای خود را بررسی می‌کنیم. توجه داشته باشید که به ازای هر سرویس درستی دسترسی به API و پاسخ دریافتی از آن API به ازای هر url در تصاویر زیر بررسی شده است. در گام نخست درستی اجرای سرویس user را بررسی می‌کنیم.

![Untitled](https://github.com/alivanaki/SE_Lab5/assets/58647313/de68b664-6bbd-4495-81dd-6cc8dd185bda)
![Untitled2](https://github.com/alivanaki/SE_Lab5/assets/58647313/c02f0901-48ab-4c85-bddb-1703f46b9245)
![Untitled3](https://github.com/alivanaki/SE_Lab5/assets/58647313/e8c64368-d81b-417d-aea9-448053d87976)
![Untitled4](https://github.com/alivanaki/SE_Lab5/assets/58647313/82e4d23e-471e-4e3b-bf70-d5e9f5f41bb9)

حال درستی اجرای سرویس data را بررسی می‌کنیم.

![Untitled_1](https://github.com/alivanaki/SE_Lab5/assets/58647313/f4bce4b3-ca98-495b-8699-c5bc2aeba535)

![Untitled_2](https://github.com/alivanaki/SE_Lab5/assets/58647313/f0c999d7-0935-4ef0-a793-8a9b039843c5)

![Untitled_3](https://github.com/alivanaki/SE_Lab5/assets/58647313/1ed1eb8b-a5d2-4d4e-ac7a-334534b1658d)

![Untitled_4](https://github.com/alivanaki/SE_Lab5/assets/58647313/dfe52032-9fef-4177-b466-c9d18fd085a8)




