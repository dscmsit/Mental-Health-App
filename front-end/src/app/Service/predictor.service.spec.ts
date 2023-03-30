import { TestBed } from '@angular/core/testing';

import { PredictorService } from './predictor.service';

describe('PredictorService', () => {
  let service: PredictorService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PredictorService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
