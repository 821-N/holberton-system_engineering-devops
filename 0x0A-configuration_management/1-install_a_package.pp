# install puppet-lint
package { 'puppet-lint':
  ensure   => '2.2.1',
  provider => 'gem',
}