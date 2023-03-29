import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-doctor-card',
  templateUrl: './doctor-card.component.html',
  styleUrls: ['./doctor-card.component.css']
})
export class DoctorCardComponent {

  // readonly FETCH_URL = "https://mentalhealthbackend.onrender.com"
  // readonly FETCH_URL2 = "https://192.168.45.111"

  // DocList: any;


  // constructor(private http: HttpClient){}

  // getDoc(){
  //   this.http.get(this.FETCH_URL+"/fetch_doc").subscribe((result) => {
  //     console.log(result);
  //     this.DocList = result; 
  //   });;
  // }
}
