// import { Component } from '@angular/core';
// import { Button } from '@material-ui/core';

// @Component({
//   selector: 'app-log-in',
//   templateUrl: './log-in.component.html',
//   styleUrls: ['./log-in.component.css']
// })
// export class LogInComponent {

// }

import { Button } from '@material-ui/core';
import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-log-in',
  templateUrl: './log-in.component.html',
  styleUrls: ['./log-in.component.css']
})
export class LogInComponent implements OnInit{
  ngOnInit(): void {
    throw new Error('Method not implemented.');
  }
  constructor(public fb: FormBuilder, private http:HttpClient ) {}
  loginForm = this.fb.group({
    email: ['', [Validators.required]],
    password: ['', [Validators.required]],
  });
  get email(){
    return this.loginForm.get('email');
  }
  get password(){
    return this.loginForm.get('password');
  }
  onSubmit(){
    const data=JSON.stringify(this.loginForm.value);
    const newUser={
      "header": "login",
      "data": data
    }

    // console.warn(data);
    this.http.post("https://mentalhealthbackend.onrender.com/login",newUser,{
      headers:{
        "Content-Type": "application/json",
      }
    }).subscribe((result)=>{
      console.log(result);
    });
  }

}
