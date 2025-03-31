import time
import threading
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import MyModel  

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal running in thread: {threading.current_thread().name}")
    time.sleep(2)  
    print("Signal execution completed")
