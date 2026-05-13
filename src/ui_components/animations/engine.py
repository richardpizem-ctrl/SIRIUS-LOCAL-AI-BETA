# SIRIUS LOCAL AI – ui_components/animations/engine.py
# AnimationEngine 1.0 – minimal, čistý základ pre AI ORB a ďalšie animácie

from typing import Protocol, List


class Animatable(Protocol):
    """
    Všetko, čo sa má animovať (AI ORB, prstence, pulzy, UI prvky),
    musí implementovať metódu update(delta_time).
    """
    def update(self, delta_time: float) -> None:
        ...


class AnimationEngine:
    """
    Jednoduchý 1.0 engine:
    - drží zoznam animovateľných objektov
    - pri každom frame volá update(delta_time) na všetkých
    """

    def __init__(self) -> None:
        # Registry všetkých animovateľných objektov
        self._objects: List[Animatable] = []
        self._running: bool = True

    def add_object(self, obj: Animatable) -> None:
        """Zaregistruje nový animovateľný objekt (napr. AI ORB)."""
        if obj not in self._objects:
            self._objects.append(obj)

    def remove_object(self, obj: Animatable) -> None:
        """Odstráni objekt z animácií."""
        if obj in self._objects:
            self._objects.remove(obj)

    def clear(self) -> None:
        """Vyčistí všetky animovateľné objekty."""
        self._objects.clear()

    def stop(self) -> None:
        """Zastaví animácie (napr. pri vypnutí UI)."""
        self._running = False

    def start(self) -> None:
        """Znovu spustí animácie."""
        self._running = True

    def update(self, delta_time: float) -> None:
        """
        Volá sa z hlavného UI loopu.
        delta_time = čas od posledného frame (v sekundách).
        """
        if not self._running:
            return

        # Prejdi všetky registrované objekty a aktualizuj ich stav
        for obj in list(self._objects):
            obj.update(delta_time)
