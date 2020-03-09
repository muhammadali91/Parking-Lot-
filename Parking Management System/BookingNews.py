from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class BookingNews(ABC):
    """
    The BookingNews interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, ParkingUpdate: ParkingUpdate) -> None:
        """
        Attach an ParkingUpdate to the BookingNews.
        """
        pass

    @abstractmethod
    def detach(self, ParkingUpdate: ParkingUpdate) -> None:
        """
        Detach an ParkingUpdate from the BookingNews.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all ParkingUpdate about an event.
        """
        pass


class ConcreteBookingNews(BookingNews): # Professor this is #
    """
    The BookingNews owns some important state and notifies ParkingUpdate when the state
    changes.
    """

    _state: int = None
    """
    For the sake of simplicity, the BookingNews's state, essential to all Parking subcribers 
    subscribers, is stored in this variable.
    """

    _ParkingUpdate: List[ParkingUpdate] = [] # by sms or email #
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def attach(self, ParkingUpdate: ParkingUpdate) -> None:
        print("BookingNews: Attached an ParkingUpdate.")
        self._ParkingUpdate.append(ParkingUpdate)

    def detach(self, ParkingUpdate: ParkingUpdate) -> None:
        self._ParkingUpdate.remove(ParkingUpdate)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("BookingNews: Welcome to Our Parking Management System ...")
        for ParkingUpdate in self._ParkingUpdate:
            ParkingUpdate.update(self)

    def some_business_logic(self) -> None:
        

        print("\nBookingNews: Thank you for Slot Reservation.")
        self._state = randrange(0, 10)

        print(f"BookingNews: 50 % Discount for Student and Sinor Citizen : {self._state}")
        self.notify()


class ParkingUpdate(ABC):
    """
    The ParkingUpdate interface declares the update method, used by BookingNews.
    """

    @abstractmethod
    def update(self, BookingNews: BookingNews) -> None:
        """
        Customer Receive update from BookingNews.
        """
        pass


"""
Concrete ParkingUpdate (Email/Sms ParkingUpdate )react to the updates issued by the BookingNews they had been
attached to.
"""


class EmailSubscribe(ParkingUpdate):
    def update(self, BookingNews: BookingNews) -> None:
        if BookingNews._state < 3:
            print("EmailSubscribe: Your Parking Slot A 4 and Time 13:45 to 14:45")


class SmsSubscribe(ParkingUpdate):
    def update(self, BookingNews: BookingNews) -> None:
        if BookingNews._state == 0 or BookingNews._state >= 2:
            print("SmsSubscribe: Your Parking Slot A 4 and Time 13:45 to 14:45")


if __name__ == "__main__":
    # The client code.

    BookingNews = ConcreteBookingNews()

    ParkingUpdate_a = EmailSubscribe()
    BookingNews.attach(ParkingUpdate_a)

    ParkingUpdate_b = SmsSubscribe()
    BookingNews.attach(ParkingUpdate_b)

    BookingNews.some_business_logic()
    BookingNews.some_business_logic()

    BookingNews.detach(ParkingUpdate_a)

    BookingNews.some_business_logic()