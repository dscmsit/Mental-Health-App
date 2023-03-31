import { Component, OnInit } from '@angular/core';
import { DoctorCardComponent } from '../doctor-card/doctor-card.component';
import { PredictorService } from '../../Service/predictor.service';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { config } from 'rxjs';

@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.css'],
})
export class ResultComponent{
  cards:any;
  result:any;
  data:any;
  state="delhi";
   id=localStorage.getItem('user_id')

  
  constructor(private predictor:PredictorService, private http:HttpClient, private router: Router){
   
     this.result = predictor.fetchedResult;
    this.result = JSON.parse(this.result);

    console.log(this.result);
    // console.log("Before api call"); 
   
    // console.log("After api call"); 
    // console.log(predictor.fetchedResult);
  }

  ngOnInit(): void {
    if (localStorage.getItem('login_status') === null){
      this.router.navigate(['/sign-in']);
    }

    this.http.get(`https://mentalhealthbackend.onrender.com/get_user/${this.id}`).subscribe((result)=>{
      // console.warn(result);
      // console.warn("hello user")
      // this.state=result;
      // JSON.stringify(this.state);
      localStorage.setItem('state',JSON.stringify(result));
      this.data = localStorage.getItem(('state'))
      // this.state = JSON.parse(this.data.state);
      this.data = JSON.parse(this.data);
      // console.log(this.data.state); 
      this.state = this.data.state;

      // console.log((localStorage.getItem(state)));
      
    })

    this.http.get(`https://mentalhealthbackend.onrender.com/fetch_doc/${this.state}`, {
      headers: {
        'Content-Type': 'application/json',
      },
    })
    .subscribe((result) => {
      // console.log(result);
      this.cards = result; 
      // console.log(this.cards);

    }); 
    // throw new Error('Method not implemented.');
  }
}
