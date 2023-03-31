import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';



@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit{
  constructor(private http:HttpClient, private router:Router){}

  data:any

  ngOnInit(): void {
      const id=localStorage.getItem('user_id')
      console.warn(id)
      
      this.http.get(`https://mentalhealthbackend.onrender.com/get_user/${id}`).subscribe((result)=>{
        console.warn(result);
        console.warn("hello user")
        this.data=result
        console.warn(this.data)
        
      })
  }

  LogOut(){
    localStorage.removeItem('login_status');
    localStorage.removeItem('user_id');
    console.log("local login status found - ",localStorage.getItem('login_status'));
    console.log("local user id found - ",localStorage.getItem('user_id'));
    this.router.navigate(['sign-in']);
    // window.location.reload();

    setTimeout(()=>{
     window.location.reload();

    },2000)
  }

}
