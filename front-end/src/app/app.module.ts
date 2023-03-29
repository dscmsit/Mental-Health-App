import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {NgCircleProgressModule} from 'ng-circle-progress';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavbarComponent } from './Components/navbar/navbar.component';
import { LogInComponent } from './Components/log-in/log-in.component';
import { SignUpComponent } from './Components/sign-up/sign-up.component';
import { HomeComponent } from './Components/home/home.component';
import { UserFormComponent } from './Components/user-form/user-form.component';
import { CardComponent } from './Components/card/card.component';

import { HttpClientModule } from '@angular/common/http';

import { FormsModule } from '@angular/forms';
import { ProfileComponent } from './Components/profile/profile.component';
import { DoctorCardComponent } from './Components/doctor-card/doctor-card.component';
import { ResultComponent } from './Components/result/result.component';
import { ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    LogInComponent,
    SignUpComponent,
    HomeComponent,
    UserFormComponent,
    CardComponent,
    ProfileComponent,
    DoctorCardComponent,
    ResultComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    NgCircleProgressModule.forRoot({
      // set defaults here
      radius: 100,
      outerStrokeWidth: 16,
      innerStrokeWidth: 8,
      outerStrokeColor: "#78C000",
      innerStrokeColor: "#C7E596",
      animationDuration: 300,
    
    })
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
