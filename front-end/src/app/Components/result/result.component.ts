import { Component } from '@angular/core';
import { DoctorCardComponent } from '../doctor-card/doctor-card.component';
import {PredictorService} from '../../Service/predictor.service'


@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.css']
})
export class ResultComponent {
  result={}; 
constructor(private predictor:PredictorService){
  this.result = predictor.fetchedResult;
console.log(this.result);


}
}
