import { Component } from '@angular/core';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent {
  constructor(){}

  LogOut(){
    localStorage.removeItem('login_status');
    localStorage.removeItem('user_id');
    console.log("local login status found - ",localStorage.getItem('login_status'));
    console.log("local user id found - ",localStorage.getItem('user_id'));
  }

}
