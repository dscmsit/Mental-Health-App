import { Component } from '@angular/core';
import { DoctorCardComponent } from '../doctor-card/doctor-card.component';
import {PredictorService} from '../../Service/predictor.service'
import { HttpClient } from '@angular/common/http';



@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.css']
})

// 

export class ResultComponent {
  result={}; 
  cards:any;
  ngOnInit(){
    console.log("Before api call"); 
    this.http.get('https://mentalhealthbackend.onrender.com/fetch_doc', {
      headers: {
        'Content-Type': 'application/json',
      },
    })
    .subscribe((result) => {
      console.log(result);
      this.cards = result;
      console.log(this.cards);
    }); 
    console.log("After api call"); 

  }
constructor(private predictor:PredictorService, private http:HttpClient){
  this.result = predictor.fetchedResult;
// console.log(this.result);

}


}
