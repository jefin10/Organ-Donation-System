
from django.db import models

class Hospital(models.Model):
    hospital_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255,default="Unnamed")
    address = models.CharField(max_length=255,null=True,blank=False)
    phone_no = models.CharField(max_length=25,default="Add phone number")
    def __str__(self):
        return self.Name

class Donor(models.Model):
    Donor_id = models.AutoField(primary_key=True) 
    Address = models.CharField(max_length=255)
    Phone_Number = models.CharField(max_length=255)
    Name = models.CharField(max_length=45)
    def __str__(self):
        return self.Name


class Insurance(models.Model):
    insurance_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255)
    limit_amount = models.IntegerField()
    def __str__(self):
        return self.company_name


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)  
    address = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=255)
    insurance = models.ForeignKey('Insurance', on_delete=models.CASCADE)  
    def __str__(self):
        return self.name

class ConsentForm(models.Model):
    consent_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE) 
    def __str__(self):
        return f"ConsentForm {self.consent_id} for Patient {self.patient.name}"
from django.db import models

class MedicalReport(models.Model):
    medicalreport_id = models.AutoField(primary_key=True)
    allergy = models.CharField(max_length=255, blank=False, null=True)
    hereditary = models.CharField(max_length=255, blank=False, null=True)
    bloodtype = models.CharField(max_length=255, blank=False, null=True)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    def __str__(self):
        return f"Medical Report {self.medicalreport_id} for Patient {self.patient.name}"

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=15)
    dob = models.DateField()
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Consults(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    def __str__(self):
        return f"Consultation with Dr. {self.doctor.name} for Patient {self.patient.name}"

class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class Transport(models.Model):
    registration_no = models.AutoField(primary_key=True)  
    vehicle_type = models.CharField(max_length=255)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)  
    def __str__(self):
        return f"{self.vehicle_type} - {self.registration_no}"

class Organ(models.Model):
    Organ_id=models.AutoField(primary_key=True)
    Organ_name=models.CharField(max_length=100)
    organ_condition = models.CharField(max_length=50, blank=True, null=True) 
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)  
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)  
    registration_no = models.ForeignKey(Transport, on_delete=models.CASCADE)  
    def __str__(self):
        return f"{self.organ_name} - {self.organ_condition}"
    
class OrganTransplant(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)  
    organ = models.ForeignKey(Organ, on_delete=models.CASCADE)   
    def __str__(self):
        return f"Transplant of {self.organ} by Dr. {self.doctor}"
class LoginInfo(models.Model):
    username = models.CharField(max_length=150, unique=True)  # Ensuring usernames are unique
    password = models.CharField(max_length=128)  # Password will be stored as a hashed string

    def __str__(self):
        return self.username