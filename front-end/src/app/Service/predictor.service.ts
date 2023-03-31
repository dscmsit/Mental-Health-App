import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class PredictorService {
fetchedResult={};
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
      this.fetchedResult = result;
      // console.log(this.fetchedResult.?result)
    }); 
  }
}


