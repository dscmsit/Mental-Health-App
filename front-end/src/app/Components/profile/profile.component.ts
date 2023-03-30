import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit{
  constructor(private http:HttpClient){}

  ngOnInit(): void {
      const id=localStorage.getItem('user_id')
      console.warn(id)
      this.http.get(`https://mentalhealthbackend.onrender.com/get_user/${id}`).subscribe((result)=>{
        console.warn(result);
      })
  }

  LogOut(){
    localStorage.removeItem('login_status');
    localStorage.removeItem('user_id');
    console.log("local login status found - ",localStorage.getItem('login_status'));
    console.log("local user id found - ",localStorage.getItem('user_id'));
  }

}
