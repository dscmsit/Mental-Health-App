import { Component, OnInit, Input } from '@angular/core';



@Component({
  selector: 'app-doctor-card',
  templateUrl: './doctor-card.component.html',
  styleUrls: ['./doctor-card.component.css']
})
export class DoctorCardComponent implements OnInit {
  
  constructor(){
  }
  @Input()
  name!: String;
  @Input()
  desc!: String; 
  @Input()
  link!: String; 

  ngOnInit(): void {
    // throw new Error('Method not implemented.');
  }
}
