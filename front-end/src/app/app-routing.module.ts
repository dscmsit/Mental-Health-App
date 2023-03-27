import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './Components/home/home.component';
import { LogInComponent } from './Components/log-in/log-in.component';
import { ProfileComponent } from './Components/profile/profile.component';
import { ResultComponent } from './Components/result/result.component';
import { SignUpComponent } from './Components/sign-up/sign-up.component';
import { UserFormComponent } from './Components/user-form/user-form.component';

const routes: Routes = [
  {
    path: '',
    component: HomeComponent
  },
  
  {
    path:'sign-in',
    component:LogInComponent
  },
  {
    path: 'sign-up',
    component:SignUpComponent
  },
  {
    path: 'user-form',
    component:UserFormComponent
  },
  {
    path: 'profile',
    component:ProfileComponent
  },
  {
    path:'result',
    component:ResultComponent
  }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
