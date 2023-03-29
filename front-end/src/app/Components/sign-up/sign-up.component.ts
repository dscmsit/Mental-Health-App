import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.css'],
})
export class SignUpComponent implements OnInit {
  ngOnInit(): void {
    throw new Error('Method not implemented.');
  }

  Gender: any = ['Male', 'Female', 'Others'];

  constructor(public fb: FormBuilder, private http: HttpClient) {}
  registrationForm = this.fb.group({
    stateName: ['', [Validators.required]],
    genderName: ['', [Validators.required]],
    first_name: ['', [Validators.required]],
    last_name: ['', [Validators.required]],
    email: ['', [Validators.required]],
    password: ['', [Validators.required]],
    confirm_pass: ['', [Validators.required]],
    dob: ['', [Validators.required]],
    
  });

  changeGender(e: any) {
    this.genderName?.setValue(e.target.value, {
      onlySelf: true,
    });
  }
  changeState(e: any){
    this.stateName?.setValue(e.target.value,{
      onlySelf: true,
    });
  }
  // Access formcontrols getter
  get genderName() {
    return this.registrationForm.get('genderName');
  }
  get first_name() {
    return this.registrationForm.get('first_name');
  }
  get last_name() {
    return this.registrationForm.get('last_name');
  }
  get email() {
    return this.registrationForm.get('email');
  }
  get password() {
    return this.registrationForm.get('password');
  }
  get confirm_pass() {
    return this.registrationForm.get('confirm_pass');
  }
  get dob() {
    return this.registrationForm.get('dob');
  }
  get stateName(){
    return this.registrationForm.get('stateName')
  }
  onSubmit() {
    // console.warn(this.registrationForm.);
    if (
      this.registrationForm.value.confirm_pass !==
      this.registrationForm.value.password
    ) {
      // continue
      alert('passwords do not match');
    }
    console.warn(this.registrationForm.value)
    const data = JSON.stringify(this.registrationForm.value);

    // console.warn(data);
    this.http
      .post<any>('https://mentalhealthbackend.onrender.com/register', data)
      .subscribe((result) => {
        console.log(result);
      });
  }
}
