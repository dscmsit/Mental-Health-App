import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import {PredictorService} from '../../Service/predictor.service'; 
import { Router } from '@angular/router';



@Component({
  selector: 'app-user-form',
  templateUrl: './user-form.component.html',
  styleUrls: ['./user-form.component.css']
})
export class UserFormComponent {
  
 

  constructor(public fb: FormBuilder, private http: HttpClient, private predict:PredictorService, private router: Router) {
    if (localStorage.getItem('login_status') ==  null){
      this.router.navigate(['/sign-in']);
    }
  }
  registrationForm = this.fb.group({
    Age : ['', [Validators.required]],
    Gender : ['', [Validators.required]],
    family_history: ['', [Validators.required]],
    no_employees: ['', [Validators.required]],
    remote_work: ['', [Validators.required]],
    benefits: ['', [Validators.required]],
    care_options: ['', [Validators.required]],
    wellness_program: ['', [Validators.required]],
    seek_help: ['', [Validators.required]],
    anonymity: ['', [Validators.required]],
    leave: ['', [Validators.required]],
    mental_health_consequence: ['', [Validators.required]],
    coworkers: ['', [Validators.required]],

    

  });
  onSubmit(){
    console.log("Form Submitted");
     // console.warn(this.registrationForm.);
     
    const stringData = JSON.stringify(this.registrationForm.value); // data is a string you have to convert to json object
    const data = JSON.parse(stringData); // data is now a JS object

    const userData = {
      header: 'register',
      data: data,
    };

    this.predict.predictMentalHealth(userData);

    setTimeout(()=>{
      this.router.navigate(['/result']);

    },1000);

  
  }
}
