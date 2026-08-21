class Autonomy:

    def __init__(self):
        self.monitor = SystemMonitor()

        self.nav = Navigation()
        self.triage_folders = TriageFolders()
        self.term = TerminalAssistant()

        self.sender = IPCSender()
        self.receiver = IPCReceiver()

        self.guard_monitor = GuardMonitor()
        self.guard_analyzer = GuardAnalyzer()
        self.guard_rules = GuardRules()
        self.guard_alerts = GuardAlerts()

        # PROCESY, KTORÉ SA MAJÚ IGNOROVAŤ AKO DANGER (napr. systémové)
        self.safe_processes = set()
        self.safe_processes.add("wmiregistrationservice.exe")  # <<< TVOJA SITUÁCIA

        # HARD STOP FLAG
        self.hard_stop_required = False

        # TIMECORE – PILIER 0
        self.timecore = TimeCore()
        self.timecore.runtime_start()
