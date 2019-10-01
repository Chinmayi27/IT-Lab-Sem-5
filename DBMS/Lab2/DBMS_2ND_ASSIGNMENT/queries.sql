select Patient.Name, PhysicianE.Name as 'Physician Name' from Patient, PhysicianE where Patient.PCP=PhysicianE.EmployeeID and PhysicianE.EmployeeID NOT IN (Select Head from Department);


select distinct Patient.Name, PhysicianE.Name as 'Physician Name' from Patient, PhysicianE, Appointment, Nurse where PhysicianE.EmployeeID=Patient.PCP and Appointment.PrepNurse=Nurse.EmployeeID and Patient.SSN in (Select Patient from Appointment where Appointment.PrepNurse in (Select EmployeeID from Nurse where Nurse.Registered = 1) group by Patient having count(*)>1);

select Patient.Name, PhysicianE.Name as 'Physician Name' from Patient, Undergoes, PhysicianE where Patient.SSN=Undergoes.Patient and Patient.PCP=PhysicianE.EmployeeID and  Undergoes.Procedures in (Select Procedures.Code from Procedures where Procedures.Cost >=5000);

select PhysicianE.Name, PhysicianE.position, Procedures.Name, Undergoes.DateUndergoes, Patient.Name from PhysicianE, Undergoes, Procedures, Patient, Trained_In where Trained_In.Physician=PhysicianE.EmployeeID and Undergoes.Physician=PhysicianE.EmployeeId and Undergoes.Procedures=Procedures.Code and Trained_In.Treatment=Procedures.Code and Undergoes.DateUndergoes>Trained_In.CertificationExpires and Undergoes.Patient=Patient.SSN;

select distinct PhysicianE.Name from PhysicianE, Procedures, Undergoes, Trained_In where Undergoes.Physician=PhysicianE.EmployeeID and Procedures.Code=Undergoes.Procedures and (Procedures.Code not in (select Trained_In.Treatment from Trained_In where PhysicianE.EmployeeID=Trained_In.Physician) or ( Undergoes.DateUndergoes>Trained_In.CertificationExpires and Trained_In.Physician = PhysicianE.EmployeeID));







