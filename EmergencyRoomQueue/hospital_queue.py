from datetime import datetime

class Patient:
    def __init__(self, name, age, symptom, severity):
        self.name = name
        self.age = age
        self.symptom = symptom
        self.severity = int(severity)
        self.arrival_time = datetime.now()
        self.treatment_time = None  # Will be set when patient is treated

    def __str__(self):
        return f"{self.name} (Age: {self.age}, Symptom: {self.symptom}, Severity: {self.severity}, Time: {self.arrival_time.strftime('%H:%M:%S')})"

class EmergencyRoom:
    def __init__(self):
        self.queue = []
        self.treated_history = []  # Store treated patients

    def add_patient(self, patient):
        """Add a patient to the waiting queue"""
        self.queue.append(patient)

    def treat_patient(self):
        """Treat the highest priority patient and move them to history"""
        if not self.queue:
            return None
        
        # Find highest priority patient (lower severity number = higher priority)
        highest_priority = self.queue[0]
        for patient in self.queue[1:]:
            if patient.severity < highest_priority.severity:
                highest_priority = patient
            elif patient.severity == highest_priority.severity:
                # If same severity, treat the one who arrived first
                if patient.arrival_time < highest_priority.arrival_time:
                    highest_priority = patient

        # Remove from queue and add to treated history
        self.queue.remove(highest_priority)
        highest_priority.treatment_time = datetime.now()
        self.treated_history.append(highest_priority)
        
        return highest_priority

    def get_waiting_list(self):
        """Get list of patients currently waiting, sorted by priority"""
        # Sort by severity first (lower number = higher priority), then by arrival time
        return sorted(self.queue, key=lambda patient: (patient.severity, patient.arrival_time))

    def get_treated_history(self):
        """Get list of all treated patients"""
        return self.treated_history

    def get_queue_stats(self):
        """Get statistics about the current queue"""
        if not self.queue:
            return {"total": 0, "by_severity": {}}
        
        stats = {
            "total": len(self.queue),
            "by_severity": {}
        }
        
        for patient in self.queue:
            severity = patient.severity
            if severity not in stats["by_severity"]:
                stats["by_severity"][severity] = 0
            stats["by_severity"][severity] += 1
        
        return stats
