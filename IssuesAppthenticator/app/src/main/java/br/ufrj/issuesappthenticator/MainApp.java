package br.ufrj.issuesappthenticator;

import android.app.Application;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.content.Context;
import android.graphics.Color;

public class MainApp extends Application
{
  @Override
  public void onCreate() {
    super.onCreate();
    if (android.os.Build.VERSION.SDK_INT >= 26) {

      NotificationManager mNotificationManager =
          (NotificationManager) getSystemService(Context.NOTIFICATION_SERVICE);
      // The id of the channel.
      String id = "my_channel_01";
      // The user-visible name of the channel.
      CharSequence name = "channel";
      // The user-visible description of the channel.
      String description = "channel_description";
      int importance = NotificationManager.IMPORTANCE_HIGH;
      NotificationChannel mChannel = null;

      mChannel = new NotificationChannel(id, name, importance);
      // Configure the notification channel.
      mChannel.setDescription(description);
      mChannel.enableLights(true);
      // Sets the notification light color for notifications posted to this
      // channel, if the device supports this feature.
      mChannel.setLightColor(Color.RED);
      mChannel.enableVibration(true);
      mChannel.setVibrationPattern(new long[]{100, 200, 300, 400, 500, 400, 300, 200, 400});
      mNotificationManager.createNotificationChannel(mChannel);



    }

  }
}
