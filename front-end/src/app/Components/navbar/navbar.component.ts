import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit{
  // user = localStorage.getItem('login_status'); 
  user:any
  id:any

  constructor(){
    this.user = localStorage.getItem('login_status');
    this.id=localStorage.getItem('user_id')
    console.log(this.user);
    console.log(this.id)
    // this.ngOnInit()
  }
  ngOnInit(): void {
    
    
  }

}
