package br.ufrj.issuesappthenticator;

import android.app.IntentService;
import android.content.Intent;
import android.content.Context;

public class CheckWifi extends IntentService {

  public CheckWifi() {
    super("CheckWifi");
  }

  @Override
  protected void onHandleIntent(Intent intent) {
    System.out.println("SHOUT OUT");
  }
}
