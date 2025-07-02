import {inject} from '@angular/core';
import {CanActivateFn, Router} from "@angular/router";
import {StorageService} from "./storage.service";

export const AuthGuardService: CanActivateFn = (route, state) => {

  const router = inject(Router);
  const storageService = inject(StorageService);

  if (!storageService.isLoggedIn()) {
    router.navigate(['/login']);
    return false;
  }
  return true;

  // const currentUser = storageService.getUser();
  // if (currentUser) {
  //   return true;
  //
  // } else {
  //   router.navigate(['/register']);
  //   return false;
  // }
};
