
import { Button } from '@material-ui/core';
import { HttpClient } from '@angular/common/http';
import { FormBuilder, Validators } from '@angular/forms';
import { Component } from '@angular/core';

@Component({
  selector: 'app-log-in',
  templateUrl: './log-in.component.html',
  styleUrls: ['./log-in.component.css']
})
export class LogInComponent {
  constructor(public fb: FormBuilder, private http: HttpClient) {}
  
  loginForm = this.fb.group({
    email:['', [Validators.required]],
    password:['', [Validators.required]]
  })

  onSubmit(){
    const stringData = JSON.stringify(this.loginForm.value); // data is a string you have to convert to json object
    const data = JSON.parse(stringData); // data is now a JS object

    const userData = {
      header: 'register',
      data: data,
    };

    this.http
      .post('https://mentalhealthbackend.onrender.com/login', userData, {
        headers: {
          'Content-Type': 'application/json',
        },
      })
      .subscribe((result) => {
        console.log(result);
      });
      console.log("this is after fetch");
  }
}
