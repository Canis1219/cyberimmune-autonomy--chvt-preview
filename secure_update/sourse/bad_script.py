from time import sleep
from src.control_system import BaseControlSystem
from multiprocessing import Queue
from src.event_types import Event
from src.config import SAFETY_BLOCK_QUEUE_NAME, SECURITY_MONITOR_QUEUE_NAME

class ControlSystemImpl:
    """ControlSystem блок расчёта управления """
    _log_message = '[ИНФО][CONTROL_IMPL] ИСПОЛЬЗУЕТСЯ ВЗЛОМАННАЯ ВЕРСИЯ ПРОГРАММЫ, МАШИНКА ПОЕДЕТ НЕ ТУДА'

    def _send_speed_and_direction_to_consumers(self, speed, direction, queues_dir):
        safety_q_name = SAFETY_BLOCK_QUEUE_NAME 

        # отправка сообщения с желаемой скоростью
        event_speed = Event(
            source=BaseControlSystem.event_source_name,
            destination=safety_q_name,
            operation="set_speed",
            parameters=100
        )                

        # отправка сообщения с желаемым направлением
        event_direction = Event(
            source=BaseControlSystem.event_source_name,
            destination=safety_q_name,
            operation="set_direction",
            parameters=10
        )                     

        security_q: Queue = queues_dir.get_queue(SECURITY_MONITOR_QUEUE_NAME)

        security_q.put(event_speed)
        security_q.put(event_direction) 
        
        print(self._log_message)  

    
    def _release_cargo(self, queues_dir):
        safety_q_name = SAFETY_BLOCK_QUEUE_NAME 
        
        event_lock_cargo = Event(
            source=BaseControlSystem.event_source_name,
            destination=safety_q_name,
            operation="lock_cargo",
            parameters=None
        )                      

        security_q: Queue = queues_dir.get_queue(SECURITY_MONITOR_QUEUE_NAME)

        security_q.put(event_lock_cargo)  

        print(self._log_message) 

    def _lock_cargo(self, queues_dir):
        safety_q_name = SAFETY_BLOCK_QUEUE_NAME 
        
        event_release_cargo = Event(
            source=BaseControlSystem.event_source_name,
            destination=safety_q_name,
            operation="release_cargo",
            parameters=None
        )                      

        security_q: Queue = queues_dir.get_queue(SECURITY_MONITOR_QUEUE_NAME)

        security_q.put(event_release_cargo)   
        
        print(self._log_message) 
