package br.ufrj.issuesappthenticator;

import android.app.AlarmManager;
import android.app.PendingIntent;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.SystemClock;

public class AlarmStarter extends BroadcastReceiver {

  @Override
  public void onReceive(Context context, Intent intent) {
    System.out.println("startup");

    AlarmManager alarmMgr = (AlarmManager)context.getSystemService(Context.ALARM_SERVICE);;

    Intent checkWifiIntent = new Intent(context, MainActivity_.class);

    PendingIntent pi = PendingIntent.getBroadcast(context, 0, checkWifiIntent, 0);

    alarmMgr.setInexactRepeating(AlarmManager.ELAPSED_REALTIME_WAKEUP,
        SystemClock.elapsedRealtime() + 2000,
        5000, pi);

  }
}
