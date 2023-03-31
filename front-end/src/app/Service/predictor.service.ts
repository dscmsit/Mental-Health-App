import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class PredictorService {
fetchedResult:any;
  constructor(private http: HttpClient) {

   }
  predictMentalHealth(data:any){
    this.http
    .post('https://mentalhealthbackend.onrender.com/predict', data, {
      headers: {
        'Content-Type': 'application/json',
      },
    })
    .subscribe((result) => {
      console.log(result);
      // this.fetchedResult = result;
      localStorage.setItem('result',JSON.stringify(result));
      this.fetchedResult = localStorage.getItem('result'); 
      this.fetchedResult = JSON.parse(this.fetchedResult);
      // console.log(this.fetchedResult.result)
    }); 
  }
}


