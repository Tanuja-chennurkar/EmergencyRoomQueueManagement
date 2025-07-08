
from datetime import datetime

class Patient:
    def __init__(self, name, age, symptom, severity):
        self.name = name
        self.age = age
        self.symptom = symptom
        self.severity = int(severity)
        self.arrival_time = datetime.now()

    def __str__(self):
        return f"{self.name} (Age: {self.age}, Symptom: {self.symptom}, Severity: {self.severity}, Time: {self.arrival_time.strftime('%H:%M:%S')})"

class EmergencyRoom:
    def __init__(self):
        self.queue = []

    def add_patient(self, patient):
        self.queue.append(patient)

    def treat_patient(self):
        if not self.queue:
            return None
        
        
        highest_priority = self.queue[0]
        for patient in self.queue[1:]:
            if patient.severity < highest_priority.severity:
                highest_priority = patient
            elif patient.severity == highest_priority.severity:
                if patient.arrival_time < highest_priority.arrival_time:
                    highest_priority = patient

        self.queue.remove(highest_priority)
        return highest_priority

    def get_waiting_list(self):
        return self.queue
