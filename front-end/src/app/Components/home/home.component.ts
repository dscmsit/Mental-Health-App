import { Component } from '@angular/core';
// import { NavbarComponent } from '../navbar/navbar.component';
import { CardComponent } from '../card/card.component';
import { Router } from '@angular/router';
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  constructor(private router: Router){
    if (localStorage.getItem('login_status') ==  null){
      this.router.navigate(['/sign-in']);
    }
  }

}
