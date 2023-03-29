import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent {
  constructor(private http:HttpClient){}
  data: any;
  onSubmit(){

    this.http.get("https://mentalhealthbackend.onrender.com/get_user").subscribe((result)=>{

      console.log(typeof result);
      this.data=result;
      for(let val of this.data){
        console.log(val)
      }
    })
  }
}
