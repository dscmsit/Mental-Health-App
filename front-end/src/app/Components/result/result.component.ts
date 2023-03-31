import { Component, OnInit } from '@angular/core';
import { DoctorCardComponent } from '../doctor-card/doctor-card.component';
import { PredictorService } from '../../Service/predictor.service';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.css'],
})
export class ResultComponent{
  cards:any;
  result=0;
  
  constructor(private predictor:PredictorService, private http:HttpClient, private router: Router){
   
    // this.result = predictor.fetchedResult.result;

    // console.log(this.result);
    // console.log("Before api call"); 
   
    // console.log("After api call"); 
    // console.log(predictor.fetchedResult);
  }

  ngOnInit(): void {
    if (localStorage.getItem('login_status') === null){
      this.router.navigate(['/sign-in']);
    }


    this.http.get('https://mentalhealthbackend.onrender.com/fetch_doc/delhi', {
      headers: {
        'Content-Type': 'application/json',
      },
    })
    .subscribe((result) => {
      console.log(result);
      this.cards = result; 
      console.log(this.cards);

    }); 
    // throw new Error('Method not implemented.');
  }
}
