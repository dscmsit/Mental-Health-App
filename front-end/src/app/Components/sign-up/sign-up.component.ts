import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.css']
})
export class SignUpComponent {
  constructor(private http:HttpClient){}
  onSubmit(data: any){
    this.http.post("http://127.0.0.1:5000/users",data)
    .subscribe((result)=>{
      console.log("result",result)
    })
    console.warn(data)
  }
}
