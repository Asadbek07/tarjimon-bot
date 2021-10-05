from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = "1910663617:AAGCFhwAGiiRlkkbhgq6d1VgqQq4kvdBgYc"  # Bot toekn
ADMINS = ["644230165"]  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
