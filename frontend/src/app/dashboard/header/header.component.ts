import {Component, OnInit} from '@angular/core';
import {StorageService} from "../../auth/storage.service";
import { Router } from '@angular/router';
import { CommonFunctionalityComponent } from '../../shared-features/common-functionality.component';
import { SHARED_MATERIAL_MODULES } from '../../shared-features/shared-material';


@Component({
  selector: 'app-header',
  standalone: true,
  imports: [SHARED_MATERIAL_MODULES],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})
export class HeaderComponent extends CommonFunctionalityComponent implements OnInit {
  isLoggedIn = false;

  constructor(
    private storageService: StorageService,
    public override router: Router
  ) {
      super(router);
  }

  // ngOnInit() {
  //   console.warn(this.isLoggedIn);
  //   this.isLoggedIn = this.storageService.isLoggedIn();
  //   console.warn(this.isLoggedIn);
  // }

  override ngOnInit(): void {
    this.isLoggedIn = this.storageService.isLoggedIn();
  }

  reloadCurrent(){
    this.reloadComponent(true);
  }

  loadHeaderData() {
    this.isLoggedIn = this.storageService.isLoggedIn();
  }

  goDashboard() {
    this.router.navigate(['/dashboard']);
  }

  goSetting() {
    this.router.navigate(['/setting']);
  }

  logout() {
    this.storageService.clear();
    this.reloadCurrent();
    window.location.reload();
  }
}
